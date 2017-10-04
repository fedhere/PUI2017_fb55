import numpy as np




def find_blocks(t, BINNED=False, fp_rate=0.05):
    # copy and sort the array
    #t = np.sort(t)
    # create length-(N + 1) array of cell edges

    if BINNED:
        tt=np.sort(t)
        num_points = tt.size
        edges = np.concatenate([tt[:1],0.5*(tt[1:] + tt[:-1]), tt[-1:]])
        block_length = tt[-1] - edges



        dt=np.diff(tt)
        ncp_prior = 4.0-np.log(fp_rate/(0.0136*num_points**0.478))
        #ncp_prior = 4.0
        tt_start , tt_stop= tt[0] - 0.5 * np.median(dt),tt[-1] - 0.5 * np.median(dt)
    else:
        num_points = t[0].size
        tt=np.arange(num_points)#np.arange(num_points)
        tones=np.ones(num_points)
        edges = np.concatenate([tt[:1],0.5*(tt[1:] + tt[:-1]), tt[-1:]])
        block_length = tt[-1] - edges

        nn_vec=[]
        #block_length = t[0][-1] - edges

        dt=np.diff(tt)
        dt_med=np.median(dt)
        #print "median",dt_med
        ncp_prior = fp_rate#(1.32) #- 0.577 * np.log(num_points)
        #print ncp_prior
        #ncp_prior = 4.0-np.log(fp_rate/(0.0136*num_points**0.478))
        tt_start , tt_stop= tt[0] - 0.5 * dt_med,tt[-1] - 0.5 * dt_med

    nn_vec = np.ones(num_points)
    best = np.zeros(num_points, dtype=float)
    last = np.zeros(num_points, dtype=int)
    #-----------------------------------------------------------------
    # Start with first data cell; add one cell at each iteration
    #-----------------------------------------------------------------

    if BINNED:
        for K in range(num_points):
            # Compute the width and count of the final bin for all possible
            # locations of the K^th changepoint
            width = block_length[:K + 1] - block_length[K + 1]
            count_vec = np.cumsum(nn_vec[:K + 1][::-1])[::-1]

            # evaluate fitness function for these possibilities
            fit_vec = count_vec * (np.log(count_vec) - np.log(width))
            fit_vec -= ncp_prior  # 4 comes from the prior on the number of changepoints
            fit_vec[1:] += best[:K]

            # find the max of the fitness: this is the K^th changepoint
            i_max = np.argmax(fit_vec)
            last[K] = i_max
            best[K] = fit_vec[i_max]

    else:
        for K in range(num_points):
            #print K+1,
            sum_1=np.cumsum(t[1][:K + 1][::-1])
            sum_0=np.cumsum(tones[:K + 1][::-1])
            #print sum_0[:K + 1][::-1][0],sum_1[:K + 1][::-1][0],
            fit_vec=((sum_1[:K + 1][::-1])**2)/(4*sum_0[:K + 1][::-1])
#ncp_prior*sum_0[:K + 1][::-1])
            #print fit_vec[0]
            fit_vec -= ncp_prior
            fit_vec[1:] += best[:K]

            # find the max of the fitness: this is the K^th changepoint
            i_max = np.argmax(fit_vec)
            last[K] = i_max
            best[K] = fit_vec[i_max] #we actually never use thus,
            #print best[K]


    #pl.plot(best)
    #-----------------------------------------------------------------
    # Recover changepoints by iteratively peeling off the last block
    #-----------------------------------------------------------------
    #print edges
    change_points = []# np.zeros(num_points, dtype=int)
    i_cp = num_points
    ind = last[num_points-1]
    ind=num_points
    for i_cp in range(num_points-1,-1,-1):
        #print "ind",ind
        change_points.append(ind)
        if ind == 0:
            break
        #print change_points
        ind = last[ind - 1]
    change_points = np.array(change_points)[::-1]
    #print change_points

    if not BINNED: return edges[change_points]/(max(edges[change_points])-min(edges[change_points]))*(max(t[0])-min(t[0]))+min(t[0])
    return edges[change_points]


signal_amp = 10
ncp_prior_vec = np.arange(.2,4.1,.2)
num_ncp_prior =  len(ncp_prior_vec)

print signal_amp,ncp_prior_vec,num_ncp_prior

num_tt_vec = np.array([ 8, 16, 32, 64, 128, 256, 512, 1024 ])
num_tt_use = len( num_tt_vec )

num_rand = 8*1024

num_cp_mat = np.zeros( (num_ncp_prior, num_tt_use) )
std_cp_mat = np.zeros(  (num_ncp_prior, num_tt_use) )
frac_cp_mat = np.zeros( (num_ncp_prior, num_tt_use) )
num_ncp_start = 0


print num_cp_mat ,std_cp_mat ,frac_cp_mat
num_plot = 0


data_in_num_plot = num_plot

for id_ncp in range(num_ncp_start, num_ncp_prior):

    print('======================================')

    ncp_prior_this = ncp_prior_vec[id_ncp ]
    data_in_ncp_prior = ncp_prior_this
    np.random.seed(seed=12345)

    for id_tt in range(0, num_tt_use):

        num_tt_this = num_tt_vec[ id_tt ]

        #clear cell_data
        cell_data=np.empty((num_tt_this,2))
        cell_data[ : , 1 ] = np.ones( num_tt_this )
        print cell_data

        data_in_tt = range(0, num_tt_this)
        data_in_tt_start = 1
        data_in_tt_stop  = num_tt_this

        num_cp_vec = np.zeros( num_rand)

        for id_rand in range(0, num_rand):

            xx = signal_amp + np.random.randn ( num_tt_this )

            cell_data[ :, 0 ] = xx**2
            data_in_cell_data = cell_data
            cp = find_blocks( data_in_cell_data, BINNED=False, fp_rate= 0.05)
            num_cp_vec( id_rand ) = length( cp );


        data_struc( id_ncp, id_tt ).num_cp_vec = num_cp_vec;
        num_cp_mat( id_ncp, id_tt ) = mean( num_cp_vec );
        std_cp_mat( id_ncp, id_tt ) = std( num_cp_vec );
        ii_this_bad = find( num_cp_vec > 0 );
        frac_cp_mat( id_ncp, id_tt ) = length( ii_this_bad )/num_rand;

    end

    print_progress( id_ncp, num_ncp_prior, 1, cpu_0 );

end

save calibrate_gauss


load calibrate_gauss

figure(1);clf
subplot(211)
line_use = '-';
st_use = '.';

for id_ncp = num_ncp_start: num_ncp_prior

    for id_tt = 1: num_tt_use
        num_cp_vec = data_struc( id_ncp, id_tt ).num_cp_vec;
    end

end

thresh = .05; % Signficance threshold (adjustable)
ncp_find_vec = zeros( num_tt_use, 1 );

for id_tt = 1: num_tt_use

    frac_vec = frac_cp_mat( :, id_tt );

    ii_find = find( frac_vec <= thresh );
    if isempty( ii_find )
        ncp_find_vec( id_tt ) = NaN;
    else
        ii_find = ii_find(1);
        ncp_find_vec( id_tt ) = ncp_prior_vec( ii_find );
    end

    if rem( id_tt, 3 ) == 1
        st_use = '.'; marker_size = 10;
    elseif rem( id_tt, 3 ) == 2
        st_use = '+';marker_size = 5;
    else
        st_use = 'o';marker_size = 4;
    end

    semilogy( ncp_prior_vec, frac_vec, [ line_use 'k' ])
    hold on
    set(semilogy( ncp_prior_vec, frac_vec, ['k' st_use ] ),'MarkerSize', marker_size )

end

v=axis;
v(1) = min( ncp_prior_vec ) -.1;
v(2) = max( ncp_prior_vec ) +.1;
v(3) = .001;
v(4) = 1.5;
axis(v)
ploty( thresh, '--k')
xlab('ncp\_prior')
ylab('False Positive Fraction ')
set(gca, 'TickDir','out')

subplot(212)

st_use = '.';
xx_log = log10( num_tt_vec );
yy_log = ncp_find_vec;
pp_fit = polyfit( xx_log, yy_log', 1 );
slope_fit = pp_fit(1);
xx_plot = linspace( min( xx_log )-.2, max( xx_log )+.2, 16 );
yy_plot = polyval( pp_fit, xx_plot );

set(semilogx( num_tt_vec, ncp_find_vec, [ line_use 'k' ] ),'LineWidth',1)
hold on
set(semilogx( num_tt_vec, ncp_find_vec, ['k' st_use ] ),'MarkerSize',8)

v = axis;
v(3) = min( ncp_find_vec ) - .2;;
v(4) = max( ncp_find_vec ) + .2;
axis(v)
ylab('ncp\_prior')
xlab('N ')
set(gca, 'TickDir','out')
drawnow

yy_plot = polyval( pp_fit, xx_plot );
semilogx( 10 .^xx_plot, yy_plot, '--k')

set_margins( 0, 0, 7, 7.5 );

eval(['print -deps cal_gauss.eps'])
'''
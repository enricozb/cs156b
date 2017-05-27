ulimit -n 2048

rm -r *.dta*.*

cd ../graphchi-cpp/

./toolkits/collaborative_filtering/rbm --training=../data/base.dta --validation=../data/probe.dta --test=../data/qual.dta --quiet=1 --D=200 --membudget_mb=3000 --rbm_alpha=0.001 --rbm_mult_step_dec=0.9 --min_val=1 --max_val=5 --max_iter=25 --halt_on_rmse_increase=2 --rbm_beta=0.001 --rbm_bins=6 --rbm_scaling=1

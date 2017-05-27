ulimit -n 2048

cd data
rm -r *.dta*.*

cd ../graphchi-cpp/

./toolkits/collaborative_filtering/svdpp --training=../data/base.dta --validation=../data/probe.dta --test=../data/qual.dta --quiet=1 --D=200 --membudget_mb=3000 --min_val=1 --max_val=5 --max_iter=25 --halt_on_rmse_increase=2


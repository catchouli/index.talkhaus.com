pushd data-gatherer
python3 data-gatherer.py
popd
pushd site
./build.sh
popd

echo $(date) > updated.time

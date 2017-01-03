python -u sfPP.py testPyClcLine.vrf
cat Verify.out > vrfyOutSum.txt

python -u sfPP.py testSf.vrf  || { echo " testSf.vrf Error"; exit 1;}
cat Verify.out >> vrfyOutSum.txt

python -u sfPP.py testOctn.vrf || { echo " testOctn.vrf Error"; exit 1;}
cat Verify.out >> vrfyOutSum.txt

python -u sfPP.py testTlRcGn.vrf  || { echo " testTlRcGn.vrf Error"; exit 1;}
cat Verify.out >> vrfyOutSum.txt

python -u sfPP.py testPyExcptn.vrf || { echo " testPyExcptn.vrf Error"; exit 1;}
cat Verify.out >> vrfyOutSum.txt

grep -n Error! vrfyOutSum.txt

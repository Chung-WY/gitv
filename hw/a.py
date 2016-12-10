import sys

from commands import getstatusoutput as a

if len(sys.argv) != 4 :
	print 'Please Use As <gitv.py findgrep pattern_file pattern_grep>'

else :
	if sys.argv[1] != 'findgrep' :
		print 'Wrong Command'
	else:
		files = a('git ls-files ' + a('git rev-parse --show-toplevel')[1])[1].split('\n')
		pattern = sys.argv[2]
		grep = sys.argv[3]

		for file in files :

			if pattern in file :

				f = open(file, 'r')
				c = f.read()
				f.close()
			
				i = 1

				for line in c.split('\n') :
					if grep in line :
						print file + ':' + str(i) + ':' + line.strip()
					i = i+1

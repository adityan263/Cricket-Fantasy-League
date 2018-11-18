#!/bin/sh
awk '{
	if (/database = \"*\"/)
		print "database = \"\"";
	else if (/user = \"*\"/)
		print "user = \"\"";
	else if (/password = \"*\"/) 
		print "password = \"\""; 
	else 
		print $0; 
	}'
exit 0

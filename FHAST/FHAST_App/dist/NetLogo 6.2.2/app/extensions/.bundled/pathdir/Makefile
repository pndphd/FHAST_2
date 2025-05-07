# If this Makefile is not being run from the NetLogo-6.x.x/app/extensions/pathdir
# directory, NETLOGO must be set before the make to the location of the NetLogo
# package.  E.g., in Cygwin this would be something like 
# export NETLOGO = "c:/Program Files/NetLogo 6.0.1"

ifeq ($(origin JAVA_HOME), undefined)
	JAVA_HOME = /usr
endif

ifeq ($(origin NETLOGO), undefined)
	NETLOGO = ../../..
endif

# NetLogo.jar files are now modefied by the NetLogo version number,
# e.g., netlogo-6.1.0.jar. Thus we shell to the "find" command which 
# looks in the app folder to get the .jar file name. I tried to 
# accomplish this with the wildcard function, but it doesn't seem to 
# handle cases where there are blanks in file/direcotry names, as is 
# common in Windows.
NETLOGO_JAR := "$(shell find "$(NETLOGO)"/app -name netlogo-*.jar)"
#NETLOGO_JAR := $(wildcard $(NETLOGO)/app/netlogo-*.jar)
JAVAC := "$(JAVA_HOME)/bin/javac"
SRCS := $(wildcard src/*.java)

pathdir.zip: pathdir.jar pathdir.jar.pack.gz README.md license.md PathDir.nlogo Makefile src manifest.txt
	rm -rf pathdir
	mkdir pathdir
	cp -rp pathdir.jar pathdir.jar.pack.gz README.md license.md PathDir.nlogo Makefile src manifest.txt pathdir
	zip -rv pathdir.zip pathdir
	rm -rf pathdir

pathdir.jar pathdir.jar.pack.gz: $(SRCS) manifest.txt Makefile
	rm -rf classes
	mkdir -p classes
	$(JAVAC) -g -deprecation -Xlint:all -Xlint:-serial -Xlint:-path -encoding us-ascii -source 1.8 -target 1.8 -classpath $(NETLOGO_JAR) -d classes $(SRCS)
	jar cmf manifest.txt pathdir.jar -C classes .
	pack200 --modification-time=latest --effort=9 --strip-debug --no-keep-file-order --unknown-attribute=strip pathdir.jar.pack.gz pathdir.jar
	rm -rf classes


all: clean compile run

clean: hashfunc
	rm hashfunc
	#test -f hashfunc && rm hashfunc

compile: hashfunc.c
	gcc -o hashfunc hashfunc.c

run: hashfunc
	./hashfunc


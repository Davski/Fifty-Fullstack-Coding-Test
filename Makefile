RUNFLAGS=-ea
DEBUG=-agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n
all:
	mkdir -p classes
	javac -d classes -cp ../../junit/junit-platform-console-standalone-1.8.1.jar *.java
debug-mode:
	mkdir -p classes
	javac -g -d classes -cp ../../junit/junit-platform-console-standalone-1.8.1.jar *.java
	java $(DEBUG) $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator
run:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --statistics

runfull:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --statistics --not-symbolic

test:
	java $(RUNFLAGS) -jar ../../junit/junit-platform-console-standalone-1.8.1.jar -cp classes -c org.ioopm.calculator.test.StandardTests

test_system:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator < input_system.txt > output.txt 2>&1 && diff output.txt output_expected_system.txt

test_scope:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator < input_scopes.txt > output.txt 2>&1 && diff output.txt output_expected_scopes.txt

test_scope_full:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic < input_scopes.txt > output.txt 2>&1 && diff output.txt output_expected_fullscopes.txt

test_reassignment:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic < input_reassignments.txt > output.txt 2>&1 && diff output.txt output_expected_reassignments.txt

test_fbvc:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic < input_fbvc.txt > output.txt 2>&1 && diff output.txt output_expected_fbvc.txt

test_conditional:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic < input_conditionals.txt > output.txt 2>&1 && diff output.txt output_expected_conditionals.txt

test_function:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic --statistics < input_functions.txt > output.txt 2>&1 && diff output.txt output_expected_functions.txt

test_brokeninput:
	java $(RUNFLAGS) -cp classes org.ioopm.calculator.Calculator --not-symbolic < input_brokeninputs.txt > output.txt 2>&1 && diff output.txt output_expected_brokeninputs.txt

clean:
	rm -rf classes; rm -f output.txt

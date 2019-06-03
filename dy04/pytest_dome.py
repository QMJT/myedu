import pytest

from dy04 import Shell

if __name__ == '__main__':
    pytest.main(['-s','-q','.dy04'])
    shell = Shell.Shell()

    pytest.main(['-s','-q','--alluredir','./Report/xml/','.'])

    Shell.invoke('allure generate ./dy04/Report/xml -o ./dy04/Report/html --clean')
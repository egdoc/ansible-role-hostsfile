TEST_HOSTFILE = '/etc/fakehostfile'
EXPECTED_HOSTFILE_CONTENT = """\
127.0.0.1    localhost localhost.localdomain localhost4 localhost4.localdomain4
:: 1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.0.39       feanor.lan feanor host1
192.168.0.35       fingolfin.lan fingolfin host2
"""

def test_hostfile_exists(host):
    assert host.file(TEST_HOSTFILE).is_file

def test_hostfile_owner(host):
    assert host.file(TEST_HOSTFILE).user == 'root'

def test_hostfile_group(host):
    assert host.file(TEST_HOSTFILE).group == 'root'
    
def test_hostfile_mode(host):
    assert host.file(TEST_HOSTFILE).mode == 0o644

def test_file_content(host):
    assert host.file('/etc/fakehostfile').content_string == EXPECTED_HOSTFILE_CONTENT

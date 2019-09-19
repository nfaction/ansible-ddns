import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ddclient_config(host):
    f = host.file('/etc/ddclient.conf')

    assert f.exists

    os_distribution = host.system_info.distribution
    redhat_systems = ['fedora', 'centos', 'redhat']

    if os_distribution in redhat_systems:
        assert f.user == 'ddclient'
        assert f.group == 'ddclient'
    else:
        assert f.user == 'root'
        assert f.group == 'root'

Name: tizen-iot-demo
Version:    1.0.0
Release:    0
Summary:	Tizen IoT demo
URL:	https://github.com/kooltux/tizen-iot-demo
Source: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
License: MIT
Group: Network & Connectivity/Other
Requires: mpu9250
Requires: nodejs

%description
Tizen IoT demo using 2 minnowboard max, 1 MPU9250 and 3 BT adapters

%prep
%setup -q
cp %{SOURCE1001} .

%build
# nothing to do

%install

# config file(s)
mkdir -p %{buildroot}%{_sysconfdir}/iot
install -m 0644 network.conf %{buildroot}%{_sysconfdir}/iot

# servers
mkdir -p %{buildroot}%{_datadir}/%{name}
for subdir in sensor_source local_router remote_server; do
	cp -a $subdir %{buildroot}%{_datadir}/%{name}/$subdir
done
install -m 755 start_service %{buildroot}%{_datadir}/%{name}/

# setup service
mkdir -p %{buildroot}%{_unitdir}
install -m 644 tizen-iot-demo.service %{buildroot}%{_unitdir}/

%post

systemctl enable tizen-iot-demo

# disable weston
systemctl disable display-manager
systemctl disable display-manager-run

systemctl daemon-reload

# update zypper repo
cat <<EOF >/etc/zypp/repos.d/tizen_local.repo
[tizen-local]
name=tizen-local
enabled=1
autorefresh=0
baseurl=http://lenovo01/~sdx/snapshot/Tizen_Common_devel/latest/repos/x86_64-wayland/packages/?ssl_verify=no
type=rpm-md
gpgcheck=0
EOF

sed -i 's/enabled=1/enabled=0/g' /etc/zypp/repos.d/tizen-common-x86_64-wayland-snapshot.repo

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%config %{_sysconfdir}/iot/*
%{_datadir}/%{name}/*
%{_unitdir}/*

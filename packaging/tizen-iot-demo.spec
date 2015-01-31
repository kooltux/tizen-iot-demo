Name: tizen-iot-demo
Version:    1.0.0
Release:    0
Summary:	Tizen IoT demo
URL:	https://github.com/kooltux/tizen-iot-demo
Source: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
License: MIT
Group: Network & Connectivity/Other
Requires: fbcat
Requires: mpu9250

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

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%config %{_sysconfdir}/iot/*
%{_datadir}/%{name}/*
%{_unitdir}/*

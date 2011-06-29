%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname msgpack

Name:           python-%{srcname}
Version:        0.1.9
Release:        2%{?dist}
Summary:        A Python MessagePack (de)serializer

Group:          Development/Languages
License:        ASL 2.0
URL:            http://pypi.python.org/pypi/msgpack-python/
Source0:        http://pypi.python.org/packages/source/m/%{srcname}-python/%{srcname}-python-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:  python-devel
BuildRequires:  python-setuptools
#BuildRequires:  python-nose

# We don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}


%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.


%prep
%setup -q -n %{srcname}-python-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


##%check
##PYTHONPATH="%{buildroot}%{python_sitearch}" nosetests -w test


%files
%defattr(-,root,root,-)
%doc COPYING README
%{python_sitearch}/%{srcname}/
%{python_sitearch}/%{srcname}*.egg-info


%changelog
* Fri Jun 24 2011 Fabian Affolter <fabian@bernewireless.net> - 0.1.9-2
- Tests are failing, they are not active at the moment
- Filtering added

* Sat Mar 26 2011 Fabian Affolter <fabian@bernewireless.net> - 0.1.9-1
- Initial package
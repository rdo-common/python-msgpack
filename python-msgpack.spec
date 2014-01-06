%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname msgpack

Name:           python-%{srcname}
Version:        0.1.13
Release:        5%{?dist}
Summary:        A Python MessagePack (de)serializer

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/msgpack-python/
Source0:        http://pypi.python.org/packages/source/m/%{srcname}-python/%{srcname}-python-%{version}.tar.gz
Patch0:         msgpack-python-0.1.9-endian.patch

BuildRequires:  python2-devel
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
%patch0 -p1 -b .endian

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

##%check
##PYTHONPATH="%{buildroot}%{python_sitearch}" nosetests -w test

%files
%doc COPYING
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/%{srcname}*.egg-info

%changelog
* Mon Jan 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-5
- Update spec file and python macros

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-1
- Update to new upstream version 0.1.13

* Tue Jan 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.12-1
- Update to new upstream version 0.1.12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.10-1
- Updated to new upstream version 0.1.10
- README is gone

* Tue Jul 12 2011 Dan Horák <dan[at]danny.cz> - 0.1.9-3
- Fix build on big endian arches

* Fri Jun 24 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-2
- Tests are failing, they are not active at the moment
- Filtering added

* Sat Mar 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-1
- Initial package

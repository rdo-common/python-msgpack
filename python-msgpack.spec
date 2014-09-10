%global srcname msgpack

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{srcname}
Version:        0.4.2
Release:        4%{?dist}
Summary:        A Python MessagePack (de)serializer

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/msgpack-python/
Source0:        http://pypi.python.org/packages/source/m/%{srcname}-python/%{srcname}-python-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

# We don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%if 0%{?with_python3}
%filter_provides_in %{python3_sitearch}/.*\.so$
%endif
%filter_setup
}

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        Higher level Python Zookeeper client
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.
%endif

%prep
%setup -q -n %{srcname}-python-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif


%files
%doc COPYING README.rst
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/%{srcname}*.egg-info

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc COPYING README.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}*.egg-info
%endif

%changelog
* Wed Sep 10 2014 Nejc Saje <nsaje@redhat.com> - 0.4.2-4
- Introduce python3- subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream version 0.4.2

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream version 0.4.1

* Tue Jan 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Update to latest upstream version 0.4.0

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

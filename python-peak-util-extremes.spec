%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define packagename Extremes

Name:           python-peak-util-extremes
Version:        1.1
Release:        4.1%{?dist}
Summary:        Production-quality 'Min' and 'Max' objects

Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://pypi.python.org/pypi/Extremes
Source0:        http://pypi.python.org/packages/source/E/%{packagename}/%{packagename}-%{version}.zip
Patch0:         %{name}-setup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

%description 
The peak.util.extremes module provides a production-quality implementation of
the Min and Max objects from PEP 326.  While PEP 326 was rejected for inclusion
in the language or standard library, the objects described in it are useful in
a variety of applications.  In PEAK, they have been used to implement generic
functions (in RuleDispatch and PEAK-Rules), as well as to handle scheduling and
time operations in the Trellis.  Because this has led to each project copying
the same code, we've now split the module out so it can be used independently.

%prep
%setup -q -n %{packagename}-%{version}
%patch0 -b .setup

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Sun Aug 12 2008 Luke Macken <lmacken@redhat.com> - 1.1-1
- Initial package for Fedora

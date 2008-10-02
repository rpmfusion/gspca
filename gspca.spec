Name:           gspca
Version:        1.00.20
Release:        2%{?dist}
Summary:        Common parts belonging to the gspca Webcam Kernel Module

Group:          System Environment/Kernel
License:        GPLv2+
URL:            http://mxhaard.free.fr/download.html
Source0:        http://mxhaard.free.fr/spca50x/Download/gspcav1-20071224.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       gspca-kmod >= %{version}
Provides:       gspca-kmod-common = %{version}-%{release}
BuildArch:      noarch

%description
This RPM contains the common parts belonging to the gspca Webcam Kernel Module,
which provides support for up to 260 different webcams not included in the
default kernel

%prep
%setup -c -q

%build
iconv -f ISO_8859-1 -t UTF-8 gspcav1-20071224/changelog --output gspcav1-20071224/changelog.utf8
cp -af gspcav1-20071224/changelog.utf8 gspcav1-20071224/changelog

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc gspcav1-20071224/changelog

%changelog
* Thu Oct 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.00.20-2
- rebuild for rpm fusion

* Thu Dec 27 2007 Jonathan Dieter <jdieter@gmail.com> - 1.00.20-1
- Rebase to upstream

* Mon Nov  5 2007 Thorsten Leemhuis <fedora [AT] leemhuis.info> - 1.00.18-3
- create RPM_BUILD_ROOT during install, as find-debuginfo.sh from F8
  will complain otherwise

* Sun Nov  4 2007 Jonathan Dieter <jdieter@gmail.com> - 1.00.18-2
- Spec file cleanup

* Sun Oct 28 2007 Jonathan Dieter <jdieter@gmail.com> - 1.00.18-1
- Initial release

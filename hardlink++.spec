Summary:	Rewrite in C++ of the hardlink utility
Name:		hardlink++
Version:	0.02
Release:	3
License:	GPL
Group:		Base
Source0:	http://www.sodarock.com/hardlink/%{name}-%{version}.tgz
# Source0-md5:	edca0c9b726faf50a239c1ca12aa2956
Patch0:		%{name}-stdio.patch
Patch1:		%{name}-sane-makefile.patch
Patch2:		%{name}-gcc34-optimize-help.patch
URL:		http://www.sodarock.com/hardlink/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A rewrite in C++ of the hardlink utility, which recursively parses
directory structures and creates hard links for identical files found.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D hardlink++ $RPM_BUILD_ROOT%{_bindir}/hardlink++

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/hardlink++

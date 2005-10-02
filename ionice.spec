Summary:	I/O priorites manager
Name:		ionice
Version:	0.1
Release:	0.20051002.1
License:	GPL
Group:		Applications
Source0:	http://ck.kolivas.org/apps/%{name}.c
# Source0-md5:	2b72b6523e1cc90f1ba0c26af9edb9ac
URL:		http://sammy.net/~sammy/hacks/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I/O priorites manager.

%prep
%setup -q -c -T

%build
%{__cc} %{rpmcflags} %{rpmldflags} %{SOURCE0} -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*

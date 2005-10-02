Summary:	I/O priorites manager
Name:		ionice
Version:	0.1
Release:	0.20051002.1
License:	GPL
Group:		Applications
Source0:	http://ck.kolivas.org/apps/%{name}.c
# Source0-md5:	4342fadac30504c86c8db7beefe01995
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

%define name gkermit
%define version 1.00
%define release	%mkrel 3
%define remoteversion 100

Summary:	Transfer files with the Kermit protocol
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		ftp://kermit.columbia.edu/kermit/archives/gku%{remoteversion}.tar.bz2
Patch:		gkermit-missing-errno-include.patch.bz2
License:	GPL
Group:		Networking/File transfer
BuildRoot:	%{_tmppath}/%{name}-buildroot

URL:		http://www.columbia.edu/kermit/gkermit.html

%description
gkermit is a GPL'd implementation of the Kermit protocol, developed by
Columbia University.  Kermit is often used to transfer files over serial
connections as well as through networks.  This version is quite minimal;
support for non-Kermit protocols may be found in ckermit, which is not,
unfortunately, Free Software. See the gkermit webpage for more information.

gkermit is a command line, non-interactive client.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch0 -p1

%build

%make

bzip2 -f gkermit.nr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
cp gkermit $RPM_BUILD_ROOT/%{_bindir}/
cp gkermit.nr.bz2 $RPM_BUILD_ROOT/%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc ANNOUNCE COPYING README
%{_bindir}/gkermit
%{_mandir}/man1/gkermit.nr.bz2

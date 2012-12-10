%define name gkermit
%define version 1.00
%define release	%mkrel 8
%define remoteversion 100

Summary:	Transfer files with the Kermit protocol
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		ftp://kermit.columbia.edu/kermit/archives/gku%{remoteversion}.tar.bz2
Patch0:		gkermit-missing-errno-include.patch
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
%setup

%patch0 -p1

%build
%make

bzip2 -f gkermit.nr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
cp gkermit $RPM_BUILD_ROOT/%{_bindir}/
cp gkermit.nr.bz2 $RPM_BUILD_ROOT/%{_mandir}/man1/gkermit.1.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc ANNOUNCE COPYING README
%{_bindir}/gkermit
%{_mandir}/man1/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.00-8mdv2011.0
+ Revision: 610857
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1.00-7mdv2010.1
+ Revision: 507411
- bunzip2 the patch

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.00-7mdv2009.0
+ Revision: 240763
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Lenny Cartier <lenny@mandriva.org> 1.00-5mdv2008.0
+ Revision: 23778
- Fix filelist
- Fix manpage name (Bug #16555)
- Import gkermit



* Thu Dec 05 2006 Lenny Cartier <lenny@mandriva.com> 1.00-3mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.00-2mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.00-1mdk
- from Levi Ramsey <leviramsey@linux-mandrake.com> :
	- Initial Cooker contrib
	- Contents of tarball moved to gkermit-1.00/
- add errno-missing-include.patch

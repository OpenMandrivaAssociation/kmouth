Name:		kmouth
Version:	4.10.4
Release:	1
Epoch:		2
Summary:	A type-and-say front end for speech synthesizers
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmouth/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime

%description
KMouth is a program which enables persons that cannot speak to let their
computer speak, e.g. mutal people or people who have lost their voice. It has a
text input field and speaks the sentences that you enter. It also has support
for user defined phrasebooks.

%files
%doc AUTHORS COPYING COPYING.DOC
%{_kde_bindir}/kmouth
%{_kde_applicationsdir}/kmouth.desktop
%{_kde_appsdir}/kmouth
%{_kde_configdir}/kmouthrc
%{_kde_iconsdir}/*/*/apps/kmouth.png
%{_kde_docdir}/HTML/en/kmouth
%{_kde_mandir}/man1/kmouth.1.*

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Sat Jul 21 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Sat Jul 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 198339
- Backport from Mageia to Mandriva 2010.2 for MIB users
- Merge handbook back into main package
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 mikala <mikala> 2:4.8.0-1.mga2
+ Revision: 198339
- Updating tarball to KDE 4.8.0

* Fri Jan 06 2012 mikala <mikala> 2:4.7.97-1.mga2
+ Revision: 192404
- Update tarball to KDE 4.7.97

* Fri Dec 23 2011 mikala <mikala> 2:4.7.95-1.mga2
+ Revision: 186269
- Update tarball to kde 4.7.95
- fix group

* Wed Dec 14 2011 mikala <mikala> 2:4.7.90-1.mga2
+ Revision: 181454
- imported package kmouth


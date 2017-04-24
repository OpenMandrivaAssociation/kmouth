%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		kmouth
Version:	17.04.0
Release:	1
Epoch:		2
Summary:	A type-and-say front end for speech synthesizers
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmouth/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
Requires:	kde-runtime

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
%{_kde_iconsdir}/*/*/*/*
%{_kde_docdir}/HTML/en/kmouth
%{_kde_mandir}/man1/kmouth.1.*

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		plasma6-kmouth
Version:	24.01.95
Release:	1
Summary:	A type-and-say front end for speech synthesizers
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmouth/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmouth-%{version}.tar.xz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF6Completion) cmake(KF6Config) cmake(KF6ConfigWidgets) cmake(KF6CoreAddons) cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO) cmake(KF6WidgetsAddons) cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6PrintSupport) cmake(Qt6TextToSpeech) cmake(Qt6Widgets) cmake(Qt6Xml)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)

%description
KMouth is a program which enables persons that cannot speak to let their
computer speak, e.g. mutal people or people who have lost their voice. It has a
text input field and speaks the sentences that you enter. It also has support
for user defined phrasebooks.

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.DOC
%{_sysconfdir}/xdg/kmouthrc
%{_bindir}/kmouth
%{_datadir}/applications/org.kde.kmouth.desktop
%{_datadir}/kmouth
%{_datadir}/icons/*/*/*/*
%{_datadir}/metainfo/org.kde.kmouth.appdata.xml
%{_mandir}/man1/kmouth.1*

%prep
%autosetup -p1 -n kmouth-%{?git:master}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man

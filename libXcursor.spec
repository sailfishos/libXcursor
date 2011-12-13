# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libXcursor
Summary:    X.Org X11 libXcursor runtime library
Version:    1.1.12
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:    index.theme
Source100:  libXcursor.yaml
Requires(post): /sbin/ldconfig
Requires(post): /bin/touch
Requires(post): %{_bindir}/gtk-update-icon-cache
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros)


%description
X.Org X11 libXcursor runtime library.


%package devel
Summary:    X.Org X11 libXcursor development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
X.Org X11 libXcursor development package.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/default/
cp -a %{SOURCE1} %{buildroot}%{_datadir}/icons/default/


# >> install post
# << install post



%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2
%dir %{_datadir}/icons/default
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/icons/default/index.theme
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%doc %{_mandir}/man3/Xcursor*.3*
# << files devel


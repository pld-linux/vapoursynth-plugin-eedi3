Summary:	Very slow edge directed interpolation filter for Vapoursynth
Summary(pl.UTF-8):	Bardzo wolny filtr interpolacji ukierunkowanej na krawędzie dla programu Vapoursynth
Name:		vapoursynth-plugin-eedi3
Version:	1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	https://github.com/vapoursynth/vs-eedi3-obsolete/archive/R%{version}/vs-eedi3-obsolete-R%{version}.tar.gz
# Source0-md5:	47f4c1da0b3c4a6861934d399d972b39
URL:		https://github.com/vapoursynth/vs-eedi3-obsolete
BuildRequires:	libtool >= 2:1.5
BuildRequires:	vapoursynth-devel >= 80
Requires:	vapoursynth >= 80
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vs_plugindir	%{py3_sitedir}/vapoursynth/plugins

%description
eedi3 is a very slow edge directed interpolation filter.

%description -l pl.UTF-8
eedi3 to bardzo wolny filtr interpolujący, nakierowany na krawędzie.

%prep
%setup -q -n vs-eedi3-obsolete-R%{version}

%build
libtool --tag=CC --mode=compile %{__cc} -c -o src/eedi3.lo %{rpmcflags} %{rpmcppflags} $(pkg-config --cflags vapoursynth) src/eedi3.c
libtool --tag=CC --mode=link %{__cc} -shared -module -avoid-version -o src/eedi3.la %{rpmldflags} %{rpmcflags} src/eedi3.lo -rpath %{vs_plugindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{vs_plugindir}

libtool --mode=install install src/eedi3.la $RPM_BUILD_ROOT%{vs_plugindir}

%{__rm} $RPM_BUILD_ROOT%{vs_plugindir}/eedi3.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/eedi3.rst
%{vs_plugindir}/eedi3.so

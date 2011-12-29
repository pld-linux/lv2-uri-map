Summary:	LV2 URI Map extension - mapping URIs to integers (DEPRECATED)
Summary(pl.UTF-8):	Rozszerzenie LV2 URI Map - odwzorowanie URI na liczby całkowite (PRZESTARZAŁE)
Name:		lv2-uri-map
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	d4ee9c20ac588cd11be60da5a6ac7454
URL:		http://lv2plug.in/ns/ext/uri-map/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 URI Map extension defines a simple mechanism for plugins to map
URIs to integers, usually for performance reasons (e.g. processing
events typed by URIs in real time). The expected use case is for
plugins to map URIs to integers for things they 'understand' at
instantiation time, and store those values for use in the audio thread
without doing any string comparison. This allows the extensibility of
RDF with the performance of integers (or centrally defined
enumerations).

Note: this extension is deprecated. New implementations should use LV2
URID instead.

%description -l pl.UTF-8
Rozszerzenie LV2 URI Map definiuje prosty mechanizm dla wtyczek,
pozwalający odwzorowywać URI na liczby całkowite - głównie ze względu
na wydajność (np. przetwarzanie w czasie rzeczywistym zdarzeń mających
typy definiowane przez URI). Oczekiwany przypadek użycia to
odwzorowywanie URI na liczby całkowite we wtyczkach dla elementów,
które są zrozumiałe w czasie tworzenia instancji, a następnie
zapisywanie tych wartości w celu użycia w wątku dźwiękowym bez
wykonywania żadnego porównywania łańcuchów znaków. Pozwala to na
rozszerzanie RDF-a z wydajnością liczb całkowitych (lub globalnie
zdefiniowanymi wyliczeniami).

Uwaga: to rozszerzenie jest przestarzałe. Nowe implementacje powinny
używać rozszerzenia LV2 URID.

%package devel
Summary:	Header file for LV2 URI Map extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 URI Map
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 URI Map extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 URI Map.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/uri-map.lv2
%{_libdir}/lv2/uri-map.lv2/uri-map.ttl
%{_libdir}/lv2/uri-map.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/uri-map.lv2/uri-map.h
%{_includedir}/lv2/lv2plug.in/ns/ext/uri-map
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-uri-map.pc

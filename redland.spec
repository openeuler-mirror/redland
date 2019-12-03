Name:           redland
Version:        1.0.17
Release:        17
Summary:        RDF iprovids support for the Resource Description Framework.
License:        LGPLv2+ or ASL 2.0
URL:            http://librdf.org/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz

BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  libdb-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  mysql-devel
BuildRequires:  perl-interpreter
BuildRequires:  postgresql-devel
BuildRequires:  raptor2-devel 
BuildRequires:  rasqal-devel >= 0.9.26
BuildRequires:  sqlite-devel

Obsoletes: redland-virtuoso < 1.0.17-8

%description
Redland is a set of free software C libraries that provide
support for the Resource Description Framework (RDF).

%package         devel
Summary:         Libraries and header files for programs that use Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     devel
Header files for development with Redland.

%package_help

%package         mysql
Summary:         MySQL storage support for Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     mysql
This package provides Redland's storage support for graphs in memory and
persistently with MySQL files or URIs.

%package         pgsql
Summary:         PostgreSQL storage support for Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     pgsql
This package provides Redland's storage support for graphs in memory and
persistently with PostgreSQL files or URIs.


%prep
%setup -q

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
  --enable-release \
  --disable-static \
  --with-virtuoso=no

%make_build


%install
%make_install

%delete_la 

%check
make check


%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%doc NOTICE TODO
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt
%{_libdir}/librdf.so.0*
%{_bindir}/rdfproc
%{_bindir}/redland-db-upgrade
%dir %{_datadir}/redland
%{_datadir}/redland/mysql-v1.ttl
%{_datadir}/redland/mysql-v2.ttl
%dir %{_libdir}/redland
%{_libdir}/redland/librdf_storage_sqlite.so

%files devel
%doc ChangeLog RELEASE.html
%{_bindir}/redland-config
%{_datadir}/redland/Redland.i
%{_datadir}/gtk-doc/
%{_includedir}/redland.h
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_libdir}/librdf.so
%{_libdir}/pkgconfig/redland.pc

%files help 
%doc FAQS.html LICENSE.html NEWS.html README.html TODO.html
%{_mandir}/man1/redland-config.1*
%{_mandir}/man1/redland-db-upgrade.1*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man3/redland.3*

%files mysql
%{_libdir}/redland/librdf_storage_mysql.so

%files pgsql
%{_libdir}/redland/librdf_storage_postgresql.so

%changelog
* Sat Nov 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.17-17 
- Package init

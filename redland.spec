Name:           redland
Version:        1.0.17
Release:        17
Summary:        RDF iprovids support for the Resource Description Framework.
License:        LGPLv2+ or ASL 2.0
URL:            http://librdf.org/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz

BuildRequires:  curl-devel gcc-c++ libdb-devel libtool-ltdl-devel libxml2-devel >= 2.4.0 mysql-devel
BuildRequires:  perl-interpreter postgresql-devel raptor2-devel rasqal-devel >= 0.9.26 sqlite-devel

Obsoletes: redland-virtuoso < 1.0.17-8

%description
Redland is a set of free software C libraries that provide
support for the Resource Description Framework (RDF).

%package         devel
Summary:         Libraries when using redland to do some developments
Provides:        %{name}-static = %{version}-%{release}
Obsoletes:       %{name}-static = %{version}-%{release}
%description     devel
Libs when developing with Redland.

%package         mysql
Summary:         Redland MySQL storage
Requires:        %{name}-static = %{version}-%{release}
%description     mysql
Provides mysql as storage for in Redland

%package         pgsql
Summary:         Redland PostgreSQL storage 
Requires:        %{name}-static = %{version}-%{release}
%description     pgsql
Provides PostgreSQL as storage for in Redland

%package_help

%prep
%autosetup -p1 

%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"%{_lib} %{_libdir}|' configure
%endif


%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
%configure --enable-release --disable-static --with-virtuoso=no

%make_build


%install
%make_install

%delete_la 

%check
make check


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig devel 
%postun -p /sbin/ldconfig devel 

%post -p /sbin/ldconfig mysql 
%postun -p /sbin/ldconfig mysql 

%post -p /sbin/ldconfig pgsql
%postun -p /sbin/ldconfig pgsql 

%files
%doc AUTHORS NEWS README NOTICE TODO
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt
%{_bindir}/rdfproc
%{_bindir}/redland-db-upgrade
%{_libdir}/librdf.so.0*
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
%{_includedir}/*.h
%{_libdir}/librdf.so
%{_libdir}/pkgconfig/redland.pc

%files mysql
%{_libdir}/redland/librdf_storage_mysql.so

%files pgsql
%{_libdir}/redland/librdf_storage_postgresql.so

%files help 
%doc FAQS.html LICENSE.html NEWS.html README.html TODO.html
%{_mandir}/man1/redland-config.1*
%{_mandir}/man1/redland-db-upgrade.1*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man3/redland.3*



%changelog
* Sun Dec 1 2019  jiaxiya <jiaxiyajiaxiya@168.com> - 1.0.17-17 
- Package init

%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Tree
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - represent XML data in a tree structure
Summary(pl):	%{_pearname} - prezentacja danych XML w postaci drzewa
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define		_rc		RC2
%define	_rel 2
Release:	0.%{_rc}.%{_rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	b492d88ce17ae329cdb7e9cc9ff51622
URL:		http://pear.php.net/package/XML_Tree/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0.4
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-XML_Parser >= 1.1.0
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for the building of XML data structures using a tree
representation, without the need for an extension like DOMXML.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta pozwala na budowanie struktur danych XML przy u�yciu
reprezentacji drzewiastej, bez potrzeby rozszerze� typu DOMXML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
# probably wrongly packaged
mv ./%{php_pear_dir}/data/%{_pearname}/README.txt docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%doc docs/README.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

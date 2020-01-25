%define		_class		XML
%define		_subclass	Tree
%define		_status		beta
%define		_pearname	XML_Tree
%define		subver	RC3
%define		rel 	4
Summary:	%{_pearname} - represent XML data in a tree structure
Summary(pl.UTF-8):	%{_pearname} - prezentacja danych XML w postaci drzewa
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	222028ad5f1404a785c656de3b8a206a
URL:		http://pear.php.net/package/XML_Tree/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.4
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
Requires:	php-pear-XML_Parser >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for the building of XML data structures using a tree
representation, without the need for an extension like DOMXML.

In PEAR status of this package is: %{_status}.

NOTE: This package is not maintained anymore and has been superseded.
Use XML_Serializer instead.

%description -l pl.UTF-8
Klasa ta pozwala na budowanie struktur danych XML przy użyciu
reprezentacji drzewiastej, bez potrzeby rozszerzeń typu DOMXML.

Ta klasa ma w PEAR status: %{_status}.

UWAGA: ten pakiet nie jest już utrzymywany, został zastąpiony pakietem
XML_Serializer.

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
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/Tree

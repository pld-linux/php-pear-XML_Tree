%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Tree
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_rc		b2

Summary:	%{_pearname} - represent XML data in a tree structure
Summary(pl):	%{_pearname} - prezentacja danych XML w postaci drzewa
Name:		php-pear-%{_pearname}
Version:	2.0
Release:	0.%{_rc}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	81fa9feee6adfab953728b7d67885899
URL:		http://pear.php.net/package/XML_Tree/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for the building of XML data structures using a tree
representation, without the need for an extension like DOMXML.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa ta pozwala na budowanie struktur danych XML przy u¿yciu
reprezentacji drzewiastej, bez potrzeby rozszerzeñ typu DOMXML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}%{_rc}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}%{_rc}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_rc}/{tests,README.txt}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

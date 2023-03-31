Name:		texlive-bangorcsthesis
Version:	61770
Release:	2
Summary:	Typeset a thesis at Bangor University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bangorcsthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class typesets thesis/dissertation documents for all levels
(i.e., both undergraduate and graduate students may use the
class). It also provides macros designed to optimise the
process of producing a thesis.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bangorcsthesis
%{_texmfdistdir}/tex/latex/bangorcsthesis
%doc %{_texmfdistdir}/doc/latex/bangorcsthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%global tl_name bangorcsthesis
%global tl_revision 75154

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.7
Release:	%{tl_revision}.1
Summary:	Typeset a thesis at Bangor University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bangorcsthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class typesets thesis/dissertation documents for all levels (i.e.,
both undergraduate and graduate students may use the class). It also
provides macros designed to optimise the process of producing a thesis.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bangorcsthesis
%dir %{_datadir}/texmf-dist/source/latex/bangorcsthesis
%dir %{_datadir}/texmf-dist/tex/latex/bangorcsthesis
%doc %{_datadir}/texmf-dist/doc/latex/bangorcsthesis/README
%doc %{_datadir}/texmf-dist/doc/latex/bangorcsthesis/bangorcsthesis.pdf
%doc %{_datadir}/texmf-dist/source/latex/bangorcsthesis/bangorcsthesis.dtx
%doc %{_datadir}/texmf-dist/source/latex/bangorcsthesis/bangorcsthesis.ins
%{_datadir}/texmf-dist/tex/latex/bangorcsthesis/bangorcsthesis.cls

Name:		python-fastuuid
Version:	0.14.0
Release:	1
Summary:	Python bindings to the Rust UUID library
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/thedrow/fastuuid
Source0:	https://files.pythonhosted.org/packages/source/f/fastuuid/fastuuid-%{version}.tar.gz
Source1:	cargo-vendor-for-fastuuid-%{version}.tar.xz
Source2:	cargo-config.toml
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	cargo
BuildRequires:	rust-packaging
BuildRequires:	clang
%undefine _debugsource_packages

%description
Fast UUID generation via Rust. Required by LiteLLM.

%prep
%autosetup -n fastuuid-%{version}
tar -xf %{SOURCE1}
install -D -m 0644 %{SOURCE2} .cargo/config.toml

%build

%install
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export CC=clang
export CXX=clang++
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/fastuuid
%{python_sitearch}/fastuuid-*.*-info

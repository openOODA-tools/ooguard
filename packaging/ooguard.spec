Name:           ooguard
Version:        0.1.0
Release:        1%{?dist}
Summary:        Prompt injection and destructive command guardrail filtering agent tool arguments.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooguard
Source0:        ooguard-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooguard is a sovereign, capability-bounded AGENT GUARDRAIL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooguard
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooguard-uninstall

%files
/usr/bin/ooguard
/usr/bin/ooguard-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding

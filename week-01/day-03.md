# Week 01, Day 03 - Monday, September 16, 2025

## 🎯 Today's Goals - ACHIEVED! ✅
- ✅ Set up Ubuntu Server VM for enterprise practice
- ✅ Master Linux system administration basics
- ✅ Complete OverTheWire Bandit levels 4-8
- ✅ Learn advanced file searching and text processing

## 🖥️ Lab Environment Expansion

### New VM: Ubuntu Server SOC Lab
- **Purpose**: Enterprise Linux practice, SOC operations simulation
- **Specs**: 2GB RAM, 20GB storage, SSH enabled
- **Status**: Fully operational and accessible via SSH ✅
- **Users Created**: socanalyst (admin), analyst1, analyst2
- **Services**: SSH server running, ready for remote management

### Multi-VM Environment Benefits
- **Kali Linux**: Penetration testing and security tools
- **Ubuntu Server**: Enterprise environment simulation
- **Next**: Windows VM for complete lab ecosystem

## 🔐 OverTheWire Bandit Progress

### Levels Completed Today: 4 → 8 ✅ (Total: 8 levels)
- **Level 4**: File type identification with `file` command
- **Level 5**: Complex file search with `find` (size, permissions)
- **Level 6**: System-wide search with user/group ownership
- **Level 7**: Text pattern matching with `grep`
- **Level 8**: Data analysis with `sort` and `uniq`
  
---

## **🎯 SUCCESS CHECKLIST FOR DAY 3:**

### **Technical Achievements:**
- [ ] Ubuntu Server VM installed and configured
- [ ] SSH access enabled and tested
- [ ] User management practice completed
- [ ] File permissions mastery demonstrated
- [ ] OverTheWire Bandit levels 4-8 completed
- [ ] Advanced Linux commands learned (find, grep, sort, uniq)

### **Lab Environment:**
- [ ] 2 VMs running simultaneously 
- [ ] Different OS environments for different purposes
- [ ] SSH connectivity between systems
- [ ] Professional multi-VM setup

### **Skills Development:**
- [ ] System administration basics
- [ ] Text processing and analysis
- [ ] Complex file searching
- [ ] Process management understanding
- [ ] Error handling and redirection

---

## **🚨 TROUBLESHOOTING DAY 3 ISSUES:**

### **VM Performance with Multiple VMs:**
```bash
# If system is slow:
1. Close unnecessary applications on host
2. Reduce one VM to 1.5GB RAM if needed
3. Don't run both VMs simultaneously if host has <8GB RAM
4. Take snapshots and shut down VMs when not in use

### Advanced Commands Mastered
```bash
file ./*                    # Check file types of all files
find / -user USER -group GROUP -size SIZE  # Complex file search
grep PATTERN filename       # Text pattern searching
sort file | uniq -u        # Find unique occurrences
2>/dev/null               # Error redirection (stealth mode!)

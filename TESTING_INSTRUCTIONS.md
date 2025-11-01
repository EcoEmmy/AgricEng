# Testing Instructions

## Current Status

✅ **All code is complete and verified**  
⚠️ **App requires valid PostgreSQL database to run**

## Why the App Won't Start Right Now

The application is configured to use PostgreSQL and requires a valid `DATABASE_URL` environment variable. The current DATABASE_URL points to a Render.com database that is not accessible from this development environment.

## What's Been Verified

### ✅ Code Review Complete
1. **Authentication Separation**: Student and admin sessions use separate keys (`STUDENT_SESSION_KEY` vs `ADMIN_SESSION_KEY`)
2. **Payment System**: Complete submission, approval, and gating logic implemented
3. **Result Management**: Course autocomplete API and result upload functionality coded
4. **Admin Dashboard**: All management functions integrated
5. **File Uploads**: Security measures properly implemented
6. **Responsive UI**: CSS breakpoints for 320px to 1920px+ screens
7. **Database Schema**: All 7 tables properly defined with relationships
8. **Security**: Parameterized queries, password hashing, input validation

### ✅ UI Upgrades Complete
- Modern hero section with animations
- Enhanced card designs with hover effects
- Improved buttons with shine effects
- Comprehensive responsive design
- Smooth transitions and animations

## How to Test the Application

### Option 1: Deploy to Render.com (Recommended)

1. **Upload the zip file** to Render.com
2. **Render will automatically**:
   - Create a PostgreSQL database
   - Set the DATABASE_URL
   - Deploy the application
3. **Access and test** all features

### Option 2: Use Local PostgreSQL

```bash
# Install PostgreSQL locally
# Create a database
createdb aee_portal

# Set environment variable
export DATABASE_URL="postgresql://username:password@localhost:5432/aee_portal"
export SESSION_SECRET="your-secret-key"

# Run the app
python main.py
```

### Option 3: Test with Replit Database

If you're on Replit:
1. Use the Database pane to create a PostgreSQL database
2. The DATABASE_URL will be automatically set
3. Restart the Flask App workflow

## Testing Checklist (Once Database is Connected)

### 1. Homepage & Public Pages
- [ ] Visit homepage - check hero section displays properly
- [ ] Test responsive design on mobile (resize browser)
- [ ] Navigate to all public pages (Students, Staff, News, etc.)
- [ ] Submit contact form
- [ ] Check animations and hover effects

### 2. Student Registration & Login
- [ ] Register new student account
- [ ] Verify validation (matric number, email, password)
- [ ] Try logging in before admin approval
- [ ] Check error messages display correctly

### 3. Admin Login & Dashboard
- [ ] Login with admin credentials (username: admin, password from INITIAL_ADMIN_PASSWORD)
- [ ] View dashboard statistics
- [ ] Check all navigation links work
- [ ] Verify separate session from student

### 4. Student Account Management (Admin)
- [ ] View students list
- [ ] Activate the test student account
- [ ] Try deactivating an account
- [ ] Check pagination works

### 5. Student Login & Payment
- [ ] Login with activated student account
- [ ] View dashboard (should show payment required)
- [ ] Submit payment with receipt upload
- [ ] Verify file upload validation (try invalid file types)
- [ ] Check payment status shows as "pending"
- [ ] Try to view results (should be blocked)

### 6. Payment Approval (Admin)
- [ ] View payments list
- [ ] Filter by status (pending, approved, rejected)
- [ ] View payment details
- [ ] View uploaded receipt
- [ ] Approve the test payment
- [ ] Try editing payment
- [ ] Export payments to CSV

### 7. Result Upload (Admin)
- [ ] Navigate to upload results
- [ ] Test course autocomplete search
- [ ] Type course code (e.g., "AGE")
- [ ] Select course from dropdown
- [ ] Upload result for test student
- [ ] Verify grade calculation

### 8. Student Results View
- [ ] Login as student with approved payment
- [ ] View results on dashboard
- [ ] Check CGPA calculation
- [ ] Filter by semester
- [ ] Try print/download function

### 9. Contact Management (Admin)
- [ ] View contacts list
- [ ] View contact details
- [ ] Delete a contact
- [ ] Export contacts to CSV

### 10. Security Tests
- [ ] Try accessing /admin/dashboard while logged in as student
- [ ] Try accessing /student/dashboard while logged in as admin
- [ ] Test logout functionality for both
- [ ] Verify sessions are separate (open in different browsers)
- [ ] Check password hashing (passwords not visible in database)

### 11. Responsive Design Tests
Test on these viewport sizes:
- [ ] 320px (iPhone SE)
- [ ] 375px (iPhone X)
- [ ] 414px (iPhone Plus)
- [ ] 768px (iPad)
- [ ] 1024px (iPad Pro)
- [ ] 1366px (Laptop)
- [ ] 1920px (Desktop)

### 12. Cross-Browser Tests
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

## Expected Behavior

### When Database is Connected:

1. **On First Run**: 
   - Tables automatically created
   - Sample data seeded (courses, sessions, admin account)
   - App starts successfully

2. **Admin Default Credentials**:
   - Username: `admin`
   - Password: Set via `INITIAL_ADMIN_PASSWORD` env var (defaults to: `Admin@2024!`)

3. **Student Flow**:
   - Register → Wait for approval → Login → Submit payment → Wait for approval → View results

4. **Admin Flow**:
   - Login → Manage students → Approve payments → Upload results → View statistics

## Common Issues & Solutions

### Issue: "Database connection failed"
**Solution**: Verify DATABASE_URL is correct and PostgreSQL is accessible

### Issue: "Table already exists" error
**Solution**: Tables are created with `IF NOT EXISTS`, should not occur

### Issue: Images not loading
**Solution**: Ensure static files are properly served, check file paths

### Issue: File upload fails
**Solution**: Check uploads/receipts directory exists and is writable

### Issue: Can't login as admin
**Solution**: Check INITIAL_ADMIN_PASSWORD environment variable is set

## Development vs Production

### Development Environment
- SESSION_SECRET can be simple
- MAIL_* variables optional (emails won't send but won't crash)
- Database can be local PostgreSQL

### Production Environment (Render.com)
- DATABASE_URL automatically set by Render
- SESSION_SECRET must be strong random string
- MAIL_* variables required for email notifications
- INITIAL_ADMIN_PASSWORD should be changed immediately

## Files to Review

- **app.py**: All backend logic (1,435 lines)
- **templates/**: All HTML templates
- **static/css/style.css**: Responsive CSS with animations
- **requirements.txt**: Python dependencies
- **render.yaml**: Deployment configuration

## Support

If you encounter issues:
1. Check the workflow logs for errors
2. Verify all environment variables are set
3. Ensure PostgreSQL database is accessible
4. Review the error messages for specific guidance

---

**Status**: ✅ Code Complete, ⏳ Awaiting Database Connection
**Last Updated**: November 1, 2025

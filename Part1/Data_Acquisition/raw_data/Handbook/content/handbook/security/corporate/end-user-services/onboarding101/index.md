---
title: "GitLab IT Onboarding 101"
---

## Welcome To GitLab

Congratulations on joining GitLab! This page is dedicated to the IT onboarding experience, here at GitLab we use many applications and the latest hardware to enable you to complete your work to the best of your ability! While it may seen a little bit overwhelming at the start the Team member enablement team is here to make the process as easy as possible!

## Laptop Setup: MacBook

> **IMPORTANT**: You will not have access to your work MacBook until your start date. On your start date,  please follow this guide.

### Before You Begin

You will receive an Okta activation email in your personal email. This is the first step to gaining access to GitLab's systems.

### Step 1: Activate Your Okta Account

1. On a mobile device, check your personal email for an Okta activation email.
2. Click the link in the email to set your password
3. After setting your password, your browser will redirect to the Okta Dashboard. **IMPORTANT: Do not open Gmail (G Suite SSO Mail) or any Google application (G Suite SSO Drive, G Suite SSO Calendar, G Suite SSO Account) before finishing the laptop setup process in Step 2. Opening these applications too early will lock you out of your laptop.**
4. You will receive a follow-up email from Okta with the subject **Security Method enrolled**.

### Step 2: MacBook Initial Setup

> **IMPORTANT**: If `Remote Management` is not available on your laptop, please use the [Jamf MDM Setup Guide](/handbook/security/corporate/systems/jamf/setup/) to manually enroll your device.

1. Power on your GitLab laptop
2. Complete the initial macOS setup:
   - Choose your preferred language
   - Select your country or region
   - Choose accessibility options (or click **Not Now**)
   - Select your WiFi network
   - On the **Remote Management** screen, click **Enroll**

3. Log into GitLab Okta:
   - Use the full GitLab email address (e.g., yourname@gitlab.com)
   - Enter the password you created on your personal device
   - Click **Sign in**

4. Set up your computer account:
   - Create a password for your local Mac account
   - Click **Continue**

5. Configure system settings:
   - On the **Enable Location Services** screen, check **Enable Location Services on this Mac**
   - Click **Continue**
   - On the **Touch ID** screen, click **Continue**
   - Enroll in Touch ID by placing your finger on the scanner (this is required)
   - On the **Choose Your Look** screen, select **Light,** **Dark,** or **Auto**
   - Click **Continue**

### Step 3: System Configuration

1. On the **Welcome to your new Mac!** screen, wait while applications are automatically installed
   - This should take a few minutes
   - When finished, click **Done**

2. System Restart:
   - A pop-up will inform you that your machine needs to restart within the next minute
   - Wait for the automatic restart or initiate it yourself
   - After restart, log back in

3. Enable FileVault:
   - Click **Enable Now** when prompted to enable FileVault (disk encryption)

### Step 4: Google Account Setup

1. Open Google Chrome
2. In the **Sign in to Chrome** window, click **Sign in**
3. Enter your GitLab email address
4. If Okta Verify opens, click **Not now** or close it
5. Sign in to Okta with your username and password
6. Click **Agree** on the Google Workspace policy that appears
7. On the **Verify it's you** screen, click **Continue**
8. On the **Enhanced Ad Privacy in Chrome** notice, click **Got It**
9. When you see **Your organization will manage this profile,** click **Continue**
10. On the **Turn on Sync** window, click **Yes, I'm in**

### Step 5: Okta Account Verification

1. In Chrome, go to https://gitlab.okta.com
2. When Okta Verify appears:
   - On the **Welcome to Okta Verify** window, click **Get Started**
   - In Chrome, enter your Okta password and click **Verify**
   - In the Okta Verify window, click **Enable** for **Enable Touch ID confirmation**
   - Close the **Complete** tab in Chrome

3. Complete security verification:
   - In Chrome, click **Verify it's you with a security method**
   - Select **Password** and click **Verify**
   - In Okta Verify, click **Yes, it's me** (or provide your fingerprint)

4. Set up additional security methods:
   - On the **Set up Security methods** screen, click **Set up** for **Security Key or Biometric authenticator**
   - Click **Set up** again to confirm
   - On the **Create a passkey for gitlab.okta.com** pop-up, click **Save another way**
   - Select **Your Chrome profile** followed by **Continue**

### Step 6: Access GitLab Email & GitLab.com Account

1. Access your GitLab email by clicking **G Suite SSO Mail** in Okta
2. Check your GitLab email for an email titled "**Welcome to GitLab Onboarding, `yourname`!**"
3. Follow the instructions in the email to set up your GitLab.com account and access your Onboarding Issue

### Congratulations

You have completed the initial setup process for your GitLab account and MacBook. If you encounter any issues, please contact the IT Help Desk.

## Laptop Setup: Linux

### Step 1: Activate Your Okta Account

1. On a mobile device, check your personal email for an Okta activation email.
2. Click the link in the email to set your password
3. After setting your password, your browser will redirect to the Okta Dashboard
4. You will receive a follow-up email from Okta with the subject **Security Method enrolled**

### Step 2: Okta Setup

1. On your Linux laptop, download Google Chrome
2. Open Google Chrome, and navigate to https://gitlab.okta.com
3. Complete security verification:
   - Click "Verify it's you with a security method"
   - Select "Password" and click "Verify"
4. Set up additional security methods:
   - On the "Set up Security methods" screen, click "Set up" for "Security Key or Biometric authenticator"
   - Click "Set up" again to confirm
   - On the "Create a passkey for gitlab.okta.com" pop-up, click "Continue"

### Step 3: Google Account Setup

1. Access your GitLab email by clicking **G Suite SSO Mail** in Okta
2. In the **Sign in to Chrome** window, click **Sign in**
3. Enter your GitLab email address
4. Sign in to Okta with your username and password
5. Click **Agree** on the Google Workspace policy that appears
6. On the **Verify it's you** screen, click **Continue**
7. On the **Enhanced Ad Privacy in Chrome** notice, click **Got It**
8. When you see **Your organization will manage this profile,** click **Continue**
9. On the **Turn on Sync** window, click **Yes, I'm in**

### Step 4: Access GitLab Email & GitLab.com Account

1. Check your GitLab email for an email titled "**Welcome to GitLab Onboarding, `yourname`!**"
2. Follow the instructions in the email to set up your GitLab.com account and access your Onboarding Issue

## Need Help?

If you need further assistance with setting up your laptop please join our weekly onboarding call scheduled every Tuesday (Check your Calendar!) or reach out to us in Slack in the #it_help channel.

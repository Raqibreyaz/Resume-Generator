***

# Resume Generator

A streamlined tool for instant resume creation using RenderCV with a modular data structure for quick customization.

### Overview

This tool simplifies the process of creating tailored resumes for different job applications. By separating static and dynamic information, you can quickly generate job-specific resumes without duplicating common data. Focus on content, not styling — RenderCV handles the formatting automatically.

### How It Works

The tool uses RenderCV to generate professional resumes from YAML data. Instead of maintaining multiple complete resume files, it uses a modular approach:

- **Static Information**: Store once, use everywhere
- **Dynamic Information**: Customize for each job application
- **Helper Files**: Quick reference for skills and projects you've worked on

### File Structure

```
info/
├── basic-info.yaml       # Static personal information
├── jd-specific.json      # Job-specific customizations
├── skills.json           # Available skills reference
└── projects.json         # Available projects reference
```

### Files Explained

**basic-info.yaml**

Contains information that remains constant across all resumes:
- Name
- Contact number
- Email address
- Location
- LinkedIn/GitHub profiles
- Other unchanging personal details

**jd-specific.json**

Stores information tailored to each job application:
- Resume objective/purpose
- Selected projects relevant to the position
- Skills matching the job requirements
- Any role-specific customizations

**skills.json** and **projects.json**

Helper files that maintain your complete portfolio of skills and projects. Use these as quick references when populating `jd-specific.json` for a new application.

### Prerequisites

This project uses [uv](https://github.com/astral-sh/uv) as the package manager for fast and reliable dependency management.

### Usage

1. Set up your `basic-info.yaml` with your personal information (one-time setup)
2. Review the job description you're applying for
3. Reference `skills.json` and `projects.json` to select relevant items
4. Update `jd-specific.json` with the selected skills and projects
5. Run RenderCV to generate your tailored resume

### Video Tutorial

Watch the complete walkthrough and demonstration:
[Resume Generator Demo](https://youtu.be/tjZ73XLyw_g)

The video covers the entire workflow and shows how this tool reduces resume modification time to just minutes.

### Benefits

- No duplication of static information
- Quick resume customization for different roles
- Maintain a single source of truth for personal details
- Easy to track which skills and projects you've included in each application
- Focus on content while RenderCV handles professional styling

***
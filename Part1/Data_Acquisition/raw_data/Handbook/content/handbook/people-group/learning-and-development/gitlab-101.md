---
title: GitLab Basics
---

## GitLab Basics and Terminology

This page is just a quick guide to some GitLab basics, for easy reference. For more in depth GitLab product training, check out the [Get Started with GitLab](https://university.gitlab.com/pages/getting-started) resources on GitLab University.

This comprehensive guide provides essential information for GitLab team members in non-engineering roles, covering everything from basic terminology to advanced features like epics and merge request reviews.

## What is GitLab?

GitLab is a web-based DevSecOps lifecycle tool that provides a Git-repository manager with wiki, issue-tracking, and CI/CD pipeline features. It's an all-in-one platform for software development, collaboration, and deployment.

## Essential GitLab Terminology

Understanding these terms will help you navigate and communicate effectively within GitLab:

**Board** - Visual tool to manage lists of issues organized by labels, team members, or milestones

**Branch** - A separate version of your project's code where you can make changes without affecting the main codebase

**Commit** - A saved change or set of changes to files in your project, like taking a snapshot of your work at a specific point in time

**DevSecOps** - Practices that combine software development, security, and IT operations to deliver software faster and more reliably

**Epic** - A way to organize multiple related issues and sub-epics around a common theme or goal

**Git** - The underlying version control system that tracks changes in your code over time

**Groups** - Collections of related projects that share permissions and access controls

**Issue** - The primary way to collaborate on ideas, track work, and discuss problems in GitLab

**Labels** - Tags that help organize and categorize issues and merge requests (like "bug," "feature," or "urgent")

**Local** - Your personal computer or development environment (as opposed to the GitLab server)

**Markdown** - A simple formatting language used to style text in GitLab descriptions and comments

**Merge Request (MR)** - A request to combine changes from one branch into another, allowing for code review and collaboration

**Milestones** - A way to group issues and merge requests by time period or project phase

**Project** - A repository that contains your code, documentation, and project management tools

**Source Code** - The human-readable instructions that make up a software program

## Working with Issues

### What are Issues?

Issues are GitLab's primary tool for collaboration, planning, and tracking work. Use them to discuss ideas, report bugs, plan features, or coordinate tasks.

### Creating an Issue

1. Navigate to the relevant project
2. Click "Issues" in the left sidebar
3. Click the blue "New issue" button
4. Add a descriptive title
5. Fill in the description with relevant details
6. Use the "Preview" tab to check formatting
7. Configure issue settings:
   - **Confidential**: Only use for non-public information (transparency is preferred)
   - **Assignee**: Person responsible for the issue
   - **Milestone**: Project phase or deadline
   - **Labels**: Categories for organization
   - **Weight**: Complexity or effort estimate
   - **Due date**: If applicable
8. Click "Submit issue"

### Finding the Right Project

Choose the project most relevant to your issue. For example, benefits-related issues would go in the Total Rewards project. Don't worry if you choose incorrectly - issues can be moved.

### Moving an Issue

If an issue is in the wrong project:

1. Open the issue
2. Scroll to the bottom of the right sidebar
3. Click "Move issue"
4. Search for and select the correct project
5. Click "Move"

### Commenting on Issues

- Scroll to the bottom of an issue to add a new comment
- To reply to a specific comment, click the speech bubble icon next to it
- Click the green "Comment" button when finished

### Searching for Issues

1. Go to gitlab.com and use the search bar
2. Enter your search terms
3. Select the appropriate group and project
4. Click the "Issues" tab to filter results

## Working with Merge Requests

### What are Merge Requests?

Merge Requests (MRs) let you propose changes to code and collaborate on them before they're integrated into the main project. Think of them as a formal way to say "I'd like to add these changes - please review them."

### Creating a Merge Request

The most common use case is editing the handbook:

1. Navigate to the file you want to edit
2. Click the "Edit" button
3. Make your changes using the web editor
4. Fill out the commit message
5. Choose "Create a new branch and start a merge request"
6. Add a descriptive title and description
7. Assign reviewers (typically your manager or a project maintainer)
8. Submit the merge request

### Key Merge Request Settings

**Assignee/Reviewer** - Your manager or someone with maintainer access can merge your MR

**Squash commits** - Combines all your changes into a single commit for cleaner history

**Delete source branch** - Automatically removes your working branch after merging

**Soft wrap** - Makes long lines of text easier to read in the editor

### Searching for Merge Requests

Use the same search process as issues, but select "Merge requests" instead of "Issues" in the results.

### Advanced Merge Request Features

#### Reviewing Merge Requests

Beyond creating merge requests, you can provide valuable feedback through reviews:

1. Open the merge request and click the "Changes" tab
2. Click on any line you want to comment on (look for the comment icon)
3. Write your comment and click "Start a review"
4. Add more comments by clicking "Add to review" 
5. To resolve discussions, check "Resolve thread" when replying
6. Click "Submit review" to publish all comments

#### Suggesting Code Changes

You can suggest specific changes that authors can apply with one click:

1. Click the comment icon on the line you want to change
1. Click the "Insert suggestion" icon in the toolbar
1. Edit the pre-populated code block with your suggestion
1. Click "Start a review" or "Add comment now"
1. The author can apply your suggestion directly, creating a new commit

#### Draft/WIP Merge Requests

When you're not ready for a merge request to be merged:

1. Add `WIP:` or `Draft:` to the beginning of the title
1. This prevents accidental merging
1. To update: click the pencil icon in the Changes tab, make changes, commit
1. When ready: remove the `WIP:` or `Draft:` prefix and assign to a reviewer

## Advanced GitLab Features

### Working with Epics

Epics help you manage portfolios of projects more efficiently by tracking groups of issues that share a theme across projects and milestones. They're excellent for project management and provide a high-level view of work progress.

#### Uses for Epics

- **Project/OKR Tracking**: Track related activities across multiple issues in different projects that contribute to a single goal
- **Timeline Management**: Set target start and end dates for groups of work
- **High-Level Collaboration**: Discuss ideas and scope at a strategic level
- **Health Reporting**: Monitor the status of multiple related issues

#### Creating an Epic

Epics are created at the group level:

1. Navigate to your project's group
2. Click "Epics" in the left sidebar
3. Click "New epic"
4. Enter the epic title
5. Click "Create epic"
6. Optionally mark as confidential if needed

#### Child Epics

Think of child epics like subfolders within a main folder. They help organize complex projects hierarchically.

To create a child epic:

1. Navigate to the parent epic
2. Click the "Add" dropdown button
3. Select "Add an epic"
4. Enter the title
5. Click "Create epic"

#### Linking Issues to Epics

Each issue can belong to only one epic. When you add an issue that's already linked to another epic, it automatically unlinks from the previous one.

**To add an issue to an epic:**

1. In the epic, click the "Add" dropdown
2. Select "Add an existing issue"
3. Paste the issue link or enter the issue ID
4. For multiple issues, use spacebar between entries
5. Click "Add"

**To add an epic to an issue:**

1. Open the issue
2. In the right sidebar, click "Epic"
3. Type the epic title and select from dropdown
4. The epic will now appear on the issue

### Creating New Handbook Pages

Before creating a new page, verify the information doesn't already exist or couldn't be added to an existing page.

#### Steps to Create a New Page

1. Navigate to the `www-gitlab-com` project
1. Go to: sites → handbook → source → handbook
1. Navigate to the appropriate folder for your content
1. Click the "+" icon and select "New file"
1. Name your file ending with `/index.html.md`
1. Add this header to your page:

```markdown
---
title: "[insert title of your page]"
description: "[insert a short sentence to appear as part of search results]"
---
```

1. Write your content
1. Add a commit message and click "Commit changes"
1. Update the merge request template and assign to appropriate reviewer

#### Handbook Tips

- **Finding Content**: Navigate to `www-gitlab-com` → sites → handbook → source → handbook, then browse folders alphabetically
- **Formatting Help**: Use the [markdown guide](https://handbook.gitlab.com/docs/markdown-guide/#markdown-style-guide-for-aboutgitlabcom) for formatting tips
- **Learning by Example**: Find similar content in the handbook and click "View source" to see how it's formatted
- **Tables and Complex Formatting**: Check the [People Group](/handbook/people-group) page for examples you can copy and modify

## Key Relationships Between GitLab Tools

Understanding how these tools work together:

- **Issues** are the foundation for tracking individual pieces of work
- **Epics** group related issues across multiple projects for strategic oversight  
- **Merge Requests** are how you propose and review changes to content
- **Boards** provide visual workflow management using issues and labels
- **Projects** contain all these elements and define access permissions

## Best Practices

**Transparency First** - Only mark issues as confidential when they contain truly non-public information

**Descriptive Titles** - Make titles clear and specific so others can quickly understand the purpose

**Use Labels** - Consistent labeling helps everyone find and organize work more effectively

**Assign Appropriately** - Make sure issues and MRs are assigned to people who can actually act on them

**Link Related Work** - Reference related issues and MRs to provide context and maintain connections

Remember: GitLab is designed to be collaborative and forgiving. You won't break anything by experimenting with issues and merge requests, so don't hesitate to dive in and start using these tools for your daily work.

## Getting Help

- **Documentation**: Check GitLab's official documentation for detailed guides
- **Search First**: Before creating new issues, search to see if similar ones already exist  
- **Ask Questions**: Use comments and mentions (@username) to get help from teammates
- **Practice**: The best way to learn GitLab is by using it regularly for your work
- **Handbook First**: Document in the handbook before taking action to ensure information is accessible to everyone

Remember: GitLab is designed to be collaborative and forgiving. You won't break anything by experimenting, so don't hesitate to dive in and start using these tools for your daily work.

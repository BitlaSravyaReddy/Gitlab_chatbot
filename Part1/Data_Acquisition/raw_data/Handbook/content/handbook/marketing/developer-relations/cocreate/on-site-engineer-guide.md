---
title: "Co-Create On-Site Engineer Guide"
---

## Overview

The Co-Create Program enables our customers to collaborate directly with GitLab engineers to contribute features, fixes, and enhancements to the platform. This is a GitLab-sponsored program, not a paid consulting service. As an on-site engineer, you'll spend one week working closely with customer engineers to kick off their contribution journey and establish long-term collaboration patterns.

This guide provides practical advice for making your on-site engagement successful, based on experiences from previous Co-Create engineers.

## Pre-On-Site Preparation

### Technical Preparation

- **Review the contribution scope**: Understand the specific issues or features you'll be working on
- **Familiarize yourself with customer context**: Review their GitLab usage, technical stack, and business objectives. Request access to customer project repositories if available
- **Prepare your development environment**: Ensure you can quickly set up GDK and demonstrate GitLab's development workflow. Be familiar with GDK alternatives (GDK in a Box, cloud VMs) for restricted environments
- **Do a technical spike**: Depending on the issue complexity, do a small spike yourself and prepare an implementation plan to provide focused direction
- **Identify potential blockers**: Consider security, architectural, or environment restrictions that might arise
- **Understand customer team backgrounds**: Learn which programming languages they're comfortable with (Ruby/Rails vs Go vs Java, etc.) to tailor your approach

### Communication Preparation

- **Join the onboarding session**: Participate in the pre-on-site customer onboarding to introduce yourself and understand the team
- **Establish practical communication**: Set up a communication channel that works for the customer team (WhatsApp group, Signal, phone numbers, etc.) for day-of coordination like building access, directions, or schedule changes
- **Share travel itinerary**: Exchange contact information and travel details in advance to ensure smooth arrivals and coordination
- **Verify setup requirements early**: Confirm customer teams have adequate time for GDK setup (can take 1-2 days). Set clear deadlines for environment preparation before the on-site
- **Create community forks**: Ensure necessary community forks are created upfront for contributions
- **Align on expectations**: Confirm the week's agenda, goals, and success criteria
- **Understand team dynamics**: Learn about the customer engineers' experience levels, roles, and motivation levels

## On-Site Best Practices

### Day 1: Foundation Setting

- **Start with relationship building**: Take time for introductions and understanding motivations
- **Establish clear objectives**: Collaboratively define what success looks like for the week
- **Confirm environment setup**: Verify all customer engineers have working GDK installations (expect this to take significant time if not done in advance)
- **Provide architectural overview**: Give a deep-dive into GitLab's architecture and the specific feature area you'll be working on
- **Review GitLab's contribution process**: Walk through the merge request workflow, code review standards, and community guidelines
- **Verify contributor profiles**: Remind customer contributors to sync their Organization fields in their GitLab profiles for proper attribution

### Technical Collaboration

- **Practice pair programming**: Work side-by-side rather than directing from afar
- **Explain the "why" not just the "how"**: Help customers understand GitLab's architectural decisions and patterns
- **Provide Ruby/Rails crash course if needed**: Be prepared to give a basic overview of GitLab's codebase structure, where controllers are located, etc.
- **Encourage experimentation**: Remind customers they can't break anything in GDK - experimentation is encouraged
- **Ensure consistent environments**: Try to have all customer engineers using the same GDK setup (all local, all VM, etc.) to avoid different issues
- **Prioritize engaged participants**: Assign critical path work to more motivated team members to avoid blocking others
- **Document learnings**: Capture setup instructions, gotchas, and solutions for future reference

### Communication and Facilitation

- **Be patient with different skill levels**: Not all customer engineers will have the same Ruby/Go experience
- **Encourage questions**: Create a safe environment for customers to ask about anything they don't understand
- **Adapt your teaching style**: Some learn best by doing, others by explanation - be flexible
- **Regular check-ins**: Ensure everyone feels included and that progress is on track
- **Plan for future contributions**: Schedule a discussion about continued contribution plans on the second-to-last day of the on-site
- **Build personal connections**: Consider opportunities for informal interaction outside of work hours, such as team dinners or local activities, which can strengthen relationships and collaboration (these can be expensed - check with the Contributor Success team)

## Managing Common Challenges

### Technical Challenges

- **GDK setup issues**: Have troubleshooting strategies ready for common environment problems. Be familiar with GDK in a Box for Windows environments and cloud VM alternatives for restricted setups
- **Restricted customer environments**: Government and enterprise customers often have locked-down machines, restricted internet access, and specific security requirements
- **Code complexity**: Break down complex changes into smaller, manageable pieces
- **Performance concerns**: Help customers understand when to optimize vs. when to prioritize functionality
- **Testing requirements**: Guide customers through writing appropriate tests for their contributions

### Process Challenges

- **Code review feedback**: Help customers understand that feedback is about improving code quality, not personal criticism. Be aware that GitLab's review process can feel overly rigorous and demoralizing to newcomers
- **Review timing conflicts**: The synchronous nature of Co-Create conflicts with asynchronous reviews. Coordinate with maintainers to ensure responsive reviews during the on-site week
- **Scale considerations**: For customers familiar with databases, explain how GitLab.com's scale affects implementation decisions. Show them tools like postgres.ai for query plan analysis to illustrate why seemingly simple fixes may need more consideration
- **Contribution guidelines**: Ensure customers understand sign-off requirements and community standards (note: licensing is handled by the Co-Create PM)
- **Timeline expectations**: Manage expectations about review cycles and merge timelines. Consider having a maintainer available in the same timezone

### Communication Challenges

- **Different working styles**: Adapt to customer team preferences and communication patterns
- **Variable engagement levels**: Participants can range from passive observers to highly motivated contributors - adapt your approach accordingly
- **Technical language barriers**: Explain GitLab-specific terminology and concepts clearly
- **Government/enterprise restrictions**: Some customers can't use Discord, external chat tools, or screen sharing - have alternatives ready
- **Physical logistics**: Government sites may require escorts, have restricted lunch options, or limited meeting spaces - plan accordingly
- **Remote vs. in-person dynamics**: If some team members are remote, ensure they're fully included

## Building Long-Term Success

### Knowledge Transfer

- **Document everything**: Create clear documentation of setup procedures, contribution workflows, and contact information
- **Identify champions**: Help customer teams identify who will drive future contributions
- **Establish ongoing support channels**: Set up communication paths with GitLab team members for continued collaboration after the on-site
- **Plan follow-up support**: Ensure customers know how to get help after you leave
  - Commit to 2 hours/week for 2 weeks post-visit for MR reviews and questions
  - Account for a 30-minute check-in call in your schedule 1 week after the on-site
  - Provide your GitLab handle for async questions in MR threads

### Community Integration

- **Introduce community resources**: Show customers how to use Discord, GitLab Forum, and documentation
- **Connect with relevant team members**: Introduce customers to product managers, engineers, and other contributors in their area of interest
- **Celebrate contributions**: Acknowledge their work publicly when appropriate

## Success Metrics and Follow-Up

### Measuring Engagement Success

- **Technical progress**: Code written, merge requests opened, tests passing
- **Learning outcomes**: Customer team's increased confidence with GitLab development
- **Relationship building**: Strength of ongoing communication and collaboration
- **Future commitment**: Customer team's plans for continued contribution

### Post-On-Site Activities

- **Retrospective session**: Conduct a brief retrospective with the customer team
- **Internal debrief**: Share learnings with the Co-Create team for program improvement
- **Ongoing support**: Provide limited follow-up support as customers complete their first contributions
- **Documentation updates**: Update this guide based on new learnings and experiences

## Key Principles to Remember

### Focus on Empowerment

- Your goal is to enable customer teams to contribute independently, not to do the work for them
- Teach problem-solving approaches, not just solutions
- Help customers understand GitLab's development culture and values

### Embrace the Learning Process

- Both sides should expect to learn from each other
- Customer domain expertise can provide valuable insights for GitLab's development
- Be open to feedback about GitLab's processes and tools

### Maintain Quality Standards

- Help customers understand that high code quality benefits everyone in the community
- Explain the reasoning behind GitLab's development standards
- Balance learning opportunities with maintaining our codebase quality

## Resources and Contacts

### During Your On-Site

- **Co-Create Project Manager**: Available for process questions, scheduling, and escalations
- **Product Managers**: For feature alignment and roadmap questions
- **Engineering Managers**: For technical architecture and code review guidance
- **Contributor Success Team**: For community and ongoing support questions

### For Customers

- [Contributor Platform](https://contributors.gitlab.com)
- [Contributor Documentation](https://docs.gitlab.com/ee/development/contributing/)
- [GitLab Development Kit](https://gitlab.com/gitlab-org/gitlab-development-kit)
- [Community Discord](https://discord.gg/gitlab)
- [Co-Create Issues](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=co-create)

## Tips from Experienced On-Site Engineers

> "The best person to solve an issue is the one experiencing it. Focus on enabling them to be successful rather than solving everything yourself."

*Raimund Hook*

> "Your job can get converted to babysitting MRs, babysitting the people, etc. Don't get frustrated. Just make sure you talk to them as much as you can about GitLab, how they are using it, what challenges they face."

*Vishal Tak*

> "We should definitely share itineraries and contact info in advance to ensure smoother arrivals and better planning"

*Siddharth Dungarwal*

> "The reviews were expedited, which definitely made an impact on the team on-site, motivating them to contribute more."

*Pedro Pombeiro*

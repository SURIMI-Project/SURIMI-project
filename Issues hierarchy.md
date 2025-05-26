# SURIMI Issue type hierarchy

The "issue type" of a Gihub Projects "Issue" is used to create a hierarchy in the work breakdown of the SURIMI project.
Most issue types can be found in the Grant Agreement. Only the "User Story" is not. As it is specific to Scrum.
```mermaid


flowchart TD
    Workpackage1["Workpackage"] --- Task1["Task"]
    Workpackage1["Workpackage"] --- Task2["Task"]
    Workpackage1["Workpackage"] --- Task3["Task"]
    Task1["Task"] --- Subtask1["Subtask"]
    Task1["Task"] --- Subtask2["Subtask"]
    Subtask1["Subtask"] --- Deliverable1["Deliverable"]
    Subtask2["Subtask"] --- Deliverable2["Deliverable"]
    Deliverable1 --- A@{ shape: processes, label: "User story" }
    Deliverable2 --- B@{ shape: processes, label: "User story" }
    Task2["Task"] ---- Deliverable3["Deliverable"]
    Deliverable3 --- C@{ shape: processes, label: "User story" }
    Task3["Task"] ---- Deliverable4["Deliverable"]
    Deliverable4 --- D@{ shape: processes, label: "User story" }


```

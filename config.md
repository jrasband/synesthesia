This is documentation for the synesthesia add-on's configuration, in *markdown* format.

Edit the configuration file as desired to pair tags with colors. The weights will determine which tags take precedence if there is a conflict.

Example configuration file:
```json
{
    "tag-color-weight": {
      "Mathematics": {"color": "green", "weight": 0.8},
      "Arts": {"color": "#FF0000", "weight": 0.2},
      "Science": {"color": "blue", "weight": 1.0},
      "": {"color": "#888", "weight": 0.5}
    }
  }
  ```
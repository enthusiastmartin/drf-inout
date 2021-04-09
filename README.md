## drf-inout

Support for different serializers in a view for Django Rest Framework

### Installation

```
pip install drf-inout
```

### Usage

Use `InOutSerializerMixin` in a view. Example:

```python
from drf_inout.mixins import InOutSerializerMixin


class PostListCreateView(InOutSerializerMixin, generics.GenericApiView):
    input_serializer_class = YourInSerializer # used for POST/PUT/PATCH requests
    output_serializer_class = YourOutSerializer # used for GET requests
```

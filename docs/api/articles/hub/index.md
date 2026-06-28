# Detail endpoints

Load related people, organizations, locations, images, and custom extracted data through separate detail endpoints on each article.

## Endpoints


| Method | Path                                     | Doc                                      |
| ------ | ---------------------------------------- | ---------------------------------------- |
| `GET`  | `…/articles/{article_id}/mentions`       | [List mentions](mentions.md)             |
| `GET`  | `…/articles/{article_id}/people`         | [List people](people.md)                 |
| `GET`  | `…/articles/{article_id}/organizations`  | [List organizations](organizations.md)   |
| `GET`  | `…/articles/{article_id}/locations`      | [List locations](locations.md)           |
| `GET`  | `…/articles/{article_id}/custom-records` | [List custom records](custom-records.md) |
| `GET`  | `…/articles/{article_id}/images`         | [List images](images.md)                 |


Each detail endpoint paginates independently. [List mentions](mentions.md) returns the full filtered set in one response — it is not paginated. Use [Get article](../get-article.md) first to confirm the article id, or follow from [List and search](../search.md) results.

### Which route to use


| Goal                                                          | Route                                    |
| ------------------------------------------------------------- | ---------------------------------------- |
| Up to 10 inline images on article detail                      | [Get article](../get-article.md)         |
| One mixed list of people, orgs, and locations (not paginated) | [List mentions](mentions.md)             |
| People with title, affiliation, and type fields               | [List people](people.md)                 |
| Organizations with type fields                                | [List organizations](organizations.md)   |
| Map-ready location geometry and addresses                     | [List locations](locations.md)           |
| Structured extracted records (contracts, etc.)                | [List custom records](custom-records.md) |
| Article images                                                | [List images](images.md)                 |


## Related

- [Articles overview](../index.md)
- [Get article](../get-article.md)


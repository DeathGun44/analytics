"""
GraphQL queries to later be used for fetching data from GitHub
"""


REPOS_QUERY: str = """
query($org:String!,$cursor:String){
  organization(login:$org){
    repositories(first:100, after:$cursor){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        name
      }
    }
  }
}
"""


ISSUES_QUERY: str = """
query($owner:String!,$repo:String!,$cursor:String){
  repository(owner:$owner,name:$repo){
    issues(first:100, after:$cursor){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        number
        title
        state
        createdAt
        closedAt
        labels(first:20){
          nodes{
            name
          }
        }
      }
    }
  }
}
"""

MERGED_PR_QUERY: str = """
query($owner:String!, $repo:String!, $cursor:String) {
  repository(owner:$owner, name:$repo) {
    pullRequests(
      first:100
      after:$cursor
      states:MERGED
      orderBy:{field:UPDATED_AT, direction:DESC}
    ) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        number
        mergedAt
        closingIssuesReferences(first:10) {
          nodes {
            number
            labels(first:20) {
              nodes {
                name
              }
            }
          }
        }
      }
    }
  }
}
"""
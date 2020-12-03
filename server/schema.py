import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
import server.users.schema
from graphql_auth.schema import UsersQuery, MeQuery


class Query(UsersQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(server.users.schema.AuthMutation, server.users.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)